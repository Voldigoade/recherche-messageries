---
title: Définitions utiles
description: 'Registre Phase 2 : Définitions utiles. Preuves, périmètres et inconnues
  documentaires au 14 octobre 2026.'
search:
  boost: 0.5
source_file: enquete-messageries-progress.md
source_line: 31
---

# Définitions utiles

!!! note "Registre de preuves — Phase 2"
    Ce dossier est une pièce de recherche datée. La [conclusion canonique](../resume.md) est celle du rapport final 1.0. Les synthèses antérieures et renvois à la Phase 3 restent historiques. `UNKNOWN` reste `UNKNOWN`.

- **Sécurité du contenu** : qui peut lire/authentifier le contenu en transit et au repos; E2EE ne couvre pas automatiquement les métadonnées, sauvegardes ou terminaux.
- **Confidentialité / minimisation des métadonnées** : quantité d’informations révélées par le compte, les serveurs, les relais, les notifications, le réseau et les appareils.
- **Pseudonymat** : usage d’un nom qui n’est pas le nom civil; un pseudonyme stable peut être corrélé dans le temps.
- **Unlinkability** : difficulté à relier deux profils ou deux relations; un identifiant stable, un avatar, une adresse IP ou des habitudes peuvent casser cette séparation.
- **Anonymat réseau** : difficulté à relier une activité à son adresse/réseau ou à un correspondant. Tor/onion routing réduisent certaines observations locales; les systèmes à faible latence ne protègent pas contre un observateur capable de voir/corréler les deux extrémités. [Limites Tor](https://support.torproject.org/about-tor/security/attacks-on-onion-routing/), [threat model Tor](https://spec.torproject.org/proposals/344-protocol-info-leaks.html).
- **E2EE** : le contenu est chiffré entre endpoints; cela ne rend ni le compte anonyme, ni le serveur aveugle à toute métadonnée.
