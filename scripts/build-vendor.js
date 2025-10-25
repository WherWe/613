#!/usr/bin/env node
/* Copy runtime assets from node_modules into vendor/ for static hosting (e.g., Vercel)
 * - bootstrap CSS (compiled from custom SCSS)
 * - tom-select JS + CSS
 * - @fontsource (Cardo + Noto Serif Hebrew) entire folders to preserve relative font URLs
 */

const fs = require("fs");
const path = require("path");
const sass = require("sass");

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

  // Compile custom Bootstrap SCSS
  console.log("Compiling custom Bootstrap SCSS...");
  const result = sass.compile(path.join(ROOT, "styles", "scss", "custom-bootstrap.scss"), {
    style: "compressed",
    sourceMap: false,
  });
  const bootstrapCssPath = path.join(vendor, "bootstrap", "css", "bootstrap.min.css");
  ensureDir(path.dirname(bootstrapCssPath));
  fs.writeFileSync(bootstrapCssPath, result.css);
  console.log(`Compiled SCSS -> ${bootstrapCssPath}`);

  // Bootstrap JS (bundle includes Popper for tooltips)
  copyFile(path.join(ROOT, "node_modules", "bootstrap", "dist", "js", "bootstrap.bundle.min.js"), path.join(vendor, "bootstrap", "js", "bootstrap.bundle.min.js"));

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

  // jQuery (required by Select2)
  copyFile(path.join(ROOT, "node_modules", "jquery", "dist", "jquery.min.js"), path.join(vendor, "jquery", "jquery.min.js"));

  // Select2 CSS + JS
  copyFile(path.join(ROOT, "node_modules", "select2", "dist", "css", "select2.min.css"), path.join(vendor, "select2", "css", "select2.min.css"));
  copyFile(path.join(ROOT, "node_modules", "select2", "dist", "js", "select2.min.js"), path.join(vendor, "select2", "js", "select2.min.js"));

  console.log("Vendor build complete.");
} catch (err) {
  console.error("Vendor build failed:", err);
  process.exit(1);
}
