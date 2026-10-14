---
title: Contradictions et distinctions de périmètre à conserver dans les matrices
description: 'Registre Phase 2 : Contradictions et distinctions de périmètre à conserver
  dans les matrices. Preuves, périmètres et inconnues documentaires au 14 octobre
  2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 200
---

# Contradictions et distinctions de périmètre à conserver dans les matrices

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

1. **Session appels** : l’ancienne matrice laissait plusieurs comportements d’appel comme inconnus. La FAQ fournisseur actuelle dit que les appels beta sont P2P et partagent l’IP avec le pair et un serveur STUN/TURN STF; les appels onion ne sont pas la fonction actuelle annoncée dans cette FAQ.
2. **SimpleX appels** : au contraire, le réglage par défaut actuel documenté est TURN relay; l’utilisateur peut le désactiver et autoriser P2P, exposant alors son IP au pair. Le relais voit au minimum la durée.
3. **Olvid** : spécification 2024 documente TURN-only et cache les IP entre pairs; elle ne cache pas les IP des participants au TURN. Ce point est plus établi que la formulation générale « appels TURN » du rapport précédent.
4. **Element** : « Matrix/Element » ne peut pas recevoir une note unique d’IP d’appel : Element Call/SFU actuel, appels plus anciens, client utilisé et infra auto-hébergée sont des configurations distinctes. La politique Element confirme la collecte d’IP/ID/timestamps pour Element Call.
5. **Delta Chat** : la politique et l’architecture d’appel montrent une possibilité de P2P (IP au pair) mais aussi relais et fallback; ce n’est pas à classer comme « IP masquée » par défaut sans examiner les candidats ICE.
