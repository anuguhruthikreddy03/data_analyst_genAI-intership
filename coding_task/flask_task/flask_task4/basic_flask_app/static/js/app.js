function copyToClipboard(text) {
  if (!text) return;
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text);
    return;
  }
  // Fallback
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "absolute";
  textarea.style.left = "-9999px";
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
}

document.addEventListener("click", (e) => {
  const btn = e.target.closest("[data-copy-target],[data-copy-text]");
  if (!btn) return;

  const directText = btn.getAttribute("data-copy-text");
  if (directText) {
    copyToClipboard(directText);
    btn.textContent = "Copied";
    setTimeout(() => (btn.textContent = "Copy"), 1200);
    return;
  }

  const targetSelector = btn.getAttribute("data-copy-target");
  if (!targetSelector) return;
  const el = document.querySelector(targetSelector);
  if (!el) return;
  copyToClipboard(el.value || el.textContent || "");
  btn.textContent = "Copied";
  setTimeout(() => (btn.textContent = "Copy"), 1200);
});


