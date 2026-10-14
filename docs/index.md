---
title: 'Messageries : sécurité, vie privée et pseudonymat'
description: 'Étude indépendante des messageries : sécurité, vie privée, pseudonymat
  et métadonnées. Conclusions conditionnelles, sources et limites explicites.'
search:
  boost: 2
---

# Messageries : sécurité, vie privée et pseudonymat

Recherche indépendante et évolutive sur 18 solutions de messagerie. Les conclusions dépendent de l’adversaire, de la version, des appareils et de la configuration.

**Rapport 1.0 · Dernière mise à jour : 14 octobre 2026.**

## L’essentiel en deux minutes

- **Il n’existe pas de gagnant universel.** E2EE protège le contenu ; il ne garantit ni l’anonymat ni l’absence de métadonnées.
- **Pour séparer une identité après un contact Discord : SimpleX**, si le correspondant l’accepte et si ses contraintes de configuration sont réalistes. Les relais, notifications iOS, terminaux et traces Discord restent à considérer.
- **Pour iPhone + PC : Signal est un compromis très praticable.** Masquer le numéro et désactiver sa découverte, partager un username non réutilisé et vérifier les clés améliorent le pseudonymat envers le contact. Le numéro reste nécessaire à l’inscription et connu du service.
- **Olvid et Threema évitent de donner un numéro au contact**, avec des limites de multi-appareil ; ils ne fournissent pas un anonymat réseau. Cwtch et Briar restent spécialisés, sans client iOS officiel établi ici.
- **Session est rétrogradé provisoirement pour l’assurance élevée** : le statut des corrections et retests des attaques WOOT 2026 doit être établi. Aucun service étudié ne démontre une résistance générale à un adversaire passif global.

Un appareil compromis ou déverrouillé et un destinataire qui copie les messages peuvent exposer le contenu, quelle que soit la messagerie.

[Lire les 14 conclusions du résumé](resume.md) · [Choisir selon son usage](usages.md) · [Comparer les capacités et limites](comparatif.md)

## Commencer la lecture

| Votre question | Page à consulter |
|---|---|
| Que signifient les termes et les statuts ? | [Comment lire cette étude](lecture.md) |
| Contre quel adversaire comparer ? | [Threat models](threat-models.md) |
| Qui peut observer quelles données ? | [Métadonnées](metadonnees.md) |
| Comment quitter Discord pour une conversation privée ? | [Discord → messagerie privée](discord-migration.md) |
| Qu’est-ce qui est réellement prouvé ? | [Méthodologie](methodologie.md), [audits](audits.md), [cas judiciaires](affaires.md) |
| Où vérifier les affirmations ? | [Sources](sources.md) et [registre complet Phase 2](recherche/index.md) |

## Limites à garder en tête

Pas de laboratoire réseau, pas de tests forensiques contrôlés, pas de reproduction bit à bit des binaires distribués. **UNKNOWN reste UNKNOWN.** Une déclaration du fournisseur, un résultat d’audit borné et une observation indépendante sont des preuves de nature différente.

Les scores numériques de l’ancienne Phase 3 ne sont pas les conclusions actuelles. Le [rapport final](rapport/index.md) fait référence ; le registre Phase 2 expose les preuves et leurs périmètres.

[Signaler une information obsolète ou proposer une source](contribuer.md).
