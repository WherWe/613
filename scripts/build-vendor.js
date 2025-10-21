#!/usr/bin/env node
/* Copy runtime assets from node_modules into vendor/ for static hosting (e.g., Vercel)
 * - bootstrap CSS
 * - tom-select JS + CSS
 * - @fontsource (Cardo + Noto Serif Hebrew) entire folders to preserve relative font URLs
 */

const fs = require("fs");
const path = require("path");

const ROOT = process.cwd();

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function copyDir(src, dest) {
  ensureDir(path.dirname(dest));
  fs.cpSync(src, dest, { recursive: true });
  console.log(`Copied dir: ${src} -> ${dest}`);
}

function copyFile(src, dest) {
  ensureDir(path.dirname(dest));
  fs.copyFileSync(src, dest);
  console.log(`Copied file: ${src} -> ${dest}`);
}

try {
  const vendor = path.join(ROOT, "vendor");
  ensureDir(vendor);

  // Bootstrap CSS
  copyFile(path.join(ROOT, "node_modules", "bootstrap", "dist", "css", "bootstrap.min.css"), path.join(vendor, "bootstrap", "css", "bootstrap.min.css"));

  // Tom Select CSS + JS
  copyFile(path.join(ROOT, "node_modules", "tom-select", "dist", "css", "tom-select.bootstrap5.css"), path.join(vendor, "tom-select", "css", "tom-select.bootstrap5.css"));
  copyFile(path.join(ROOT, "node_modules", "tom-select", "dist", "js", "tom-select.complete.min.js"), path.join(vendor, "tom-select", "js", "tom-select.complete.min.js"));

  // Fontsource families (copy entire dirs so CSS relative font URLs keep working)
  copyDir(path.join(ROOT, "node_modules", "@fontsource", "cardo"), path.join(vendor, "@fontsource", "cardo"));
  copyDir(path.join(ROOT, "node_modules", "@fontsource", "roboto"), path.join(vendor, "@fontsource", "roboto"));
  copyDir(path.join(ROOT, "node_modules", "@fontsource", "noto-serif-hebrew"), path.join(vendor, "@fontsource", "noto-serif-hebrew"));

  // Lucide icons
  copyFile(path.join(ROOT, "node_modules", "lucide", "dist", "umd", "lucide.min.js"), path.join(vendor, "lucide", "lucide.min.js"));

  // SweetAlert2
  copyFile(path.join(ROOT, "node_modules", "sweetalert2", "dist", "sweetalert2.all.min.js"), path.join(vendor, "sweetalert2", "sweetalert2.all.min.js"));

  console.log("Vendor build complete.");
} catch (err) {
  console.error("Vendor build failed:", err);
  process.exit(1);
}
