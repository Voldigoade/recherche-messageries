/* Pure, auditable decision rules. No scoring, network calls or stored answers. */
(function (root) {
  'use strict';
  function normaliseSelection(raw, messengers) {
    const known = new Set(messengers.map(m => m.id));
    const incoming = String(raw || 'signal,simplex').split(',');
    const ids = [...new Set(incoming.filter(id => known.has(id)))].slice(0, 4);
    if (!ids.length) ids.push('signal');
    if (ids.length === 1) ids.push(ids[0] === 'simplex' ? 'signal' : 'simplex');
    return {ids, corrected: incoming.join(',') !== ids.join(',')};
  }
  function recommend(answers, catalog) {
    if (!answers.priority) return {error: 'priority', candidates: []};
    let ruleId = answers.priority;
    const overrides = {contact:'contact', provider:'metadata', isp:'network', legal:'legal', osint:'pseudonymity', censorship:'censorship', global:'network'};
    if (overrides[answers.adversary]) ruleId = overrides[answers.adversary];
    if (answers.hide_ip === 'yes' && answers.calls === 'yes' && !['global','isp','legal','censorship','provider'].includes(answers.adversary)) ruleId = 'contact';
    const rule = catalog.rules.find(r => r.id === ruleId);
    if (!rule) return {error: 'priority', candidates: []};
    const lookup = new Map(catalog.messengers.map(m => [m.id,m]));
    const excluded = [];
    const candidates = [];
    for (const id of rule.candidates) {
      const m = lookup.get(id);
      const c = m.constraints;
      let reason;
      if (answers.iphone === 'yes' && !['yes','conditional'].includes(c.ios)) reason='ios';
      else if (answers.desktop === 'yes' && !['yes','conditional'].includes(c.desktop)) reason='desktop';
      else if (answers.phone === 'none' && c.phone !== 'optional') reason='phone';
      else if (answers.phone === 'peer' && c.phone === 'required' && m.id !== 'signal') reason='peer_number';
      else if (answers.calls === 'yes' && !['yes','conditional'].includes(c.calls)) reason='calls';
      else if (answers.calls === 'yes' && answers.hide_ip === 'yes' && c.peer_ip === 'exposed') reason='peer_ip';
      if (reason) excluded.push({id,reason});
      else candidates.push({id, conditional: c.ios === 'conditional' && answers.iphone === 'yes' || c.desktop === 'conditional' && answers.desktop === 'yes' || c.calls === 'conditional' && answers.calls === 'yes'});
    }
    return {ruleId, candidates:candidates.slice(0,3), excluded, globalWarning:answers.adversary === 'global'};
  }
  const api = {normaliseSelection,recommend};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.StudyDecision = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
