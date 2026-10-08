/* Čebelarstvo Šemen: count-up for the numbers row (section id ends with __stevilke_semen) */
(function () {
  var sec = document.querySelector('[id$="__stevilke_semen"]');
  if (!sec) return;
  var els = [].slice.call(sec.querySelectorAll('.media-body h5, .media-body h2, .media-body .h2'));
  if (!els.length) return;
  var items = els.map(function (el) {
    var m = (el.textContent || '').trim().match(/^(\d+)(.*)$/);
    if (!m) return null;
    return { el: el, target: parseInt(m[1], 10), suffix: m[2] || '' };
  }).filter(Boolean);
  if (!items.length) return;
  items.forEach(function (it) { it.el.textContent = '0' + it.suffix; });
  var done = false;
  function run() {
    if (done) return;
    done = true;
    var dur = 1600, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var e = 1 - Math.pow(1 - p, 3);
      items.forEach(function (it) { it.el.textContent = Math.round(it.target * e) + it.suffix; });
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (en) { return en.isIntersecting; })) { run(); io.disconnect(); }
    }, { threshold: 0.35 });
    io.observe(sec);
  } else {
    run();
  }
})();
