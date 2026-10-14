const test=require('node:test');
const assert=require('node:assert/strict');
const raw=require('../data/messengers.json');
const {recommend,normaliseSelection}=require('../docs/javascripts/decision.js');
const catalog={messengers:raw.messengers,rules:raw.decision_rules};
const defaults={priority:'daily',iphone:'either',desktop:'no',phone:'okay',calls:'no',hide_ip:'no',adversary:'general'};
const choose=answers=>recommend({...defaults,...answers},catalog);
const ids=result=>result.candidates.map(c=>c.id);
test('Everyday security retains the report’s ordered starting points',()=>assert.deepEqual(ids(choose({})),['signal','threema','olvid']));
test('No number at the service excludes Signal while preserving compatible alternatives',()=>assert.deepEqual(ids(choose({priority:'pseudonymity',phone:'none',iphone:'yes',desktop:'yes'})),['simplex','threema','olvid']));
test('Hiding a number only from the peer still permits hardened Signal',()=>assert.ok(ids(choose({priority:'pseudonymity',phone:'peer'})).includes('signal')));
test('Tor-oriented options are not presented as official iPhone applications',()=>assert.deepEqual(ids(choose({priority:'network',iphone:'yes'})),['simplex']));
test('Required calls exclude Briar and Cwtch and do not pad the result',()=>assert.deepEqual(ids(choose({priority:'network',calls:'yes'})),['simplex']));
test('A global observer always receives an explicit absence-of-general-resistance warning',()=>assert.equal(choose({adversary:'global'}).globalWarning,true));
test('The legal rule can return one iPhone candidate; no promise of legal immunity',()=>assert.deepEqual(ids(choose({adversary:'legal',iphone:'yes'})),['simplex']));
test('An incompatible team + no-number configuration yields no manufactured answer',()=>assert.equal(choose({priority:'teams',phone:'none'}).candidates.length,0));
test('Session is never reintroduced by any preference combination',()=>{
  for(const priority of raw.decision_rules.map(r=>r.id))for(const adversary of ['general','provider','contact','isp','legal','osint','censorship','global'])assert.ok(!ids(choose({priority,adversary})).includes('session'));
});
test('Choose a priority instead of silently guessing',()=>assert.equal(choose({priority:''}).error,'priority'));
test('Comparison parameters are limited to known, unique identifiers and four columns',()=>{
  const selection=normaliseSelection('bad,signal,signal,simplex,olvid,threema,session',raw.messengers);
  assert.deepEqual(selection.ids,['signal','simplex','olvid','threema']);assert.equal(selection.corrected,true);
});
test('Single-profile comparison links keep that messenger and add a distinct peer',()=>assert.deepEqual(normaliseSelection('simplex',raw.messengers).ids,['simplex','signal']));
