window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    macros: {
      Prob: "\\mathbb{P}",
      logit: "\\operatorname{logit}",
      softmax: "\\operatorname{softmax}",
      Ex: "\\mathbb{E}"
    }
  },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" }
};
