/* Material wraps tables after its document stream starts. Enhance those wrappers. */
function enhanceTables() {
  document.querySelectorAll('.md-typeset__scrollwrap').forEach((region) => {
    region.tabIndex = 0;
    region.setAttribute('role', 'region');
    region.setAttribute('aria-label', 'Tableau — défilement horizontal avec les flèches du clavier');
  });
}
enhanceTables();
const article = document.querySelector('article');
if (article) new MutationObserver(enhanceTables).observe(article, {childList: true, subtree: true});
window.addEventListener('load', enhanceTables, {once: true});

/* Retain Material's native checkbox toggles, expose its icon labels to keyboards. */
document.querySelectorAll('label.md-header__button[for="__drawer"], label.md-header__button[for="__search"], label.md-search__icon[for="__search"]').forEach((trigger) => {
  const control = document.getElementById(trigger.htmlFor);
  trigger.setAttribute('role', 'button');
  trigger.setAttribute('aria-label', trigger.htmlFor === '__drawer' ? 'Ouvrir la navigation' : trigger.classList.contains('md-search__icon') ? 'Fermer la recherche' : 'Ouvrir la recherche');
  trigger.tabIndex = 0;
  trigger.setAttribute('aria-expanded', String(control.checked));
  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      trigger.click();
    }
  });
  control.addEventListener('change', () => trigger.setAttribute('aria-expanded', String(control.checked)));
  trigger.querySelectorAll('svg').forEach((icon) => icon.setAttribute('aria-hidden', 'true'));
});
document.addEventListener('keydown', (event) => {
  const drawer = document.getElementById('__drawer');
  if (event.key === 'Escape' && drawer.checked) {
    drawer.click();
    document.querySelector('.md-header label[for="__drawer"]').focus();
  }
});
