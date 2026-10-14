/* Material wraps tables after its document stream starts. Enhance those wrappers. */
function enhanceTables() {
  document.querySelectorAll('table.study-table').forEach((table, index) => {
    table.setAttribute('role', 'table');
    const heads = [...table.querySelectorAll('thead th')];
    heads.forEach((head, col) => { head.scope='col'; head.id ||= 'dynamic-'+index+'-col-'+col; });
    table.querySelectorAll('thead,tbody').forEach(group => group.setAttribute('role','rowgroup'));
    table.querySelectorAll('tbody tr').forEach((row, rowIndex) => {
      row.setAttribute('role','row');
      const cells=[...row.children];
      cells[0].setAttribute('role','rowheader'); cells[0].id ||= 'dynamic-'+index+'-row-'+rowIndex;
      cells.slice(1).forEach((cell,col) => {
        if(!heads[col+1]) return;
        cell.setAttribute('role','cell'); cell.setAttribute('headers',heads[col+1].id+' '+cells[0].id);
        if(!cell.querySelector(':scope > .study-cell-label')) {
          const label=document.createElement('span'); label.className='study-cell-label';
          const anchor=heads[col+1].querySelector('a');
          if(anchor) label.append(anchor.cloneNode(true));
          else { label.textContent=heads[col+1].textContent; label.setAttribute('aria-hidden','true'); }
          cell.prepend(label);
        }
      });
    });
  });
  document.querySelectorAll('.md-typeset__scrollwrap').forEach((region) => {
    if(region.querySelector('.study-matrix')) {
      region.tabIndex=0; region.setAttribute('role','region'); region.setAttribute('aria-label',tableWords[0]);
    } else { region.removeAttribute('tabindex'); region.removeAttribute('role'); region.removeAttribute('aria-label'); }
  });
}
const tableLanguage=document.documentElement.lang.startsWith('es')?'es':document.documentElement.lang.startsWith('en')?'en':'fr';
const tableWords={fr:['Matrice — défilement horizontal avec les flèches','Ouvrir la navigation','Fermer la recherche','Ouvrir la recherche'],en:['Matrix — scroll horizontally with arrow keys','Open navigation','Close search','Open search'],es:['Matriz: desplazamiento horizontal con flechas','Abrir navegación','Cerrar búsqueda','Abrir búsqueda']}[tableLanguage];
window.StudyTables={enhance:enhanceTables};
enhanceTables();
const article = document.querySelector('article');
if (article) new MutationObserver(enhanceTables).observe(article, {childList: true, subtree: true});
window.addEventListener('load', enhanceTables, {once: true});

/* Retain Material's native checkbox toggles, expose its icon labels to keyboards. */
document.querySelectorAll('label.md-header__button[for="__drawer"], label.md-header__button[for="__search"], label.md-search__icon[for="__search"]').forEach((trigger) => {
  const control = document.getElementById(trigger.htmlFor);
  trigger.setAttribute('role', 'button');
  trigger.setAttribute('aria-label', trigger.htmlFor === '__drawer' ? tableWords[1] : trigger.classList.contains('md-search__icon') ? tableWords[2] : tableWords[3]);
  trigger.tabIndex = 0;
  trigger.setAttribute('aria-expanded', String(control.checked));
  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      event.stopPropagation();
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
