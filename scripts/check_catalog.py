"""Validate data coverage, source ranges and the unchanged canonical report."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check():
    data = json.loads((ROOT/'data/messengers.json').read_text(encoding='utf-8'))
    assert len(data['messengers']) == 18
    assert len({m['id'] for m in data['messengers']}) == 18
    assert sum(m['primary'] for m in data['messengers']) == 7
    assert hashlib.sha256((ROOT/'research'/data['report']['file']).read_bytes()).hexdigest() == data['report']['sha256'], 'Canonical report changed without review'
    for id, ref in data['sources'].items():
        lines=(ROOT/'research'/ref['file']).read_text(encoding='utf-8-sig').splitlines()
        assert 1 <= ref['start_line'] <= ref['end_line'] <= len(lines), id
        excerpt='\n'.join(lines[ref['start_line']-1:ref['end_line']]).rstrip()
        assert hashlib.sha256(excerpt.encode()).hexdigest() == ref['sha256'], f'Source range changed: {id}'
    field_ids={f['id'] for f in data['fields']}
    for m in data['messengers']:
        for key, fact in m['facts'].items():
            assert key in field_ids or key == 'platforms', (m['id'],key)
            assert set(fact['text']) == {'fr','en','es'}
            assert all(fact['text'].values()), (m['id'],key)
            assert fact['sources'] and all(r in data['sources'] for r in fact['sources'])
        for key in ('identifier','e2ee','metadata','ip','strength','weakness','best','confidence'):
            assert key in m['facts'], (m['id'],key)
    for rule in data['decision_rules']:
        assert len(set(rule['candidates'])) == len(rule['candidates'])
        assert 'session' not in rule['candidates'], 'Session high-assurance downgrade must remain visible'
        assert all(id in {m['id'] for m in data['messengers']} for id in rule['candidates'])
        assert all(ref in data['sources'] for ref in rule['sources'])
    learning=json.loads((ROOT/'content/learning.json').read_text(encoding='utf-8'))
    assert len(learning['concepts']) == 16 and len(learning['misconceptions']) == 11
    for item in learning['concepts'] + learning['misconceptions']:
        assert all(ref in data['sources'] for ref in item['sources'])
        for key,val in item.items():
            if isinstance(val,dict): assert set(val) == {'fr','en','es'} and all(val.values()), (item['id'],key)
    print('PASS: 18 profiles, 7 main candidates, 16 concepts, 11 misconceptions, FR/EN/ES, source-range hashes and unchanged report.')


if __name__ == '__main__':
    check()
