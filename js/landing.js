/**
 * LANDING PAGE - JAVASCRIPT DE INTERATIVIDADE (CASH FLOW & PRICING)
 * Gerencia Acordeão de FAQ, rolagem suave e preservação de UTMs
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. FAQ Accordion
  const faqItems = document.querySelectorAll('.lp-faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.lp-faq-question');
    const answer = item.querySelector('.lp-faq-answer');

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Fecha outros itens abertos para efeito sanfona elegante
      faqItems.forEach(other => {
        other.classList.remove('active');
        const otherAns = other.querySelector('.lp-faq-answer');
        if (otherAns) otherAns.style.maxHeight = null;
      });

      if (!isActive) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // Abre o primeiro item do FAQ por padrão
  if (faqItems.length > 0) {
    const firstItem = faqItems[0];
    const firstAnswer = firstItem.querySelector('.lp-faq-answer');
    firstItem.classList.add('active');
    if (firstAnswer) firstAnswer.style.maxHeight = firstAnswer.scrollHeight + 'px';
  }

  // 2. Rolagem suave para âncoras internas
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

  // 3. Preservação de parâmetros de rastreamento (UTM, src, sck, ref)
  const urlParams = window.location.search;
  if (urlParams) {
    const hotmartBtn = document.getElementById('btn-checkout-hotmart');
    if (hotmartBtn && hotmartBtn.href && hotmartBtn.href !== '#') {
      const sep = hotmartBtn.href.includes('?') ? '&' : '?';
      hotmartBtn.href += sep + urlParams.substring(1);
    }
    const kiwifyBtn = document.getElementById('btn-checkout-kiwify');
    if (kiwifyBtn && kiwifyBtn.href && kiwifyBtn.href !== '#') {
      const sep = kiwifyBtn.href.includes('?') ? '&' : '?';
      kiwifyBtn.href += sep + urlParams.substring(1);
    }
  }
});
