#!/usr/bin/env node
// pnpm's node_modules/.bin/tailwindcss is a POSIX shell wrapper script, but
// Hugo's css.TailwindCSS resource transform rejects anything that isn't a
// direct Node.js script (or native binary) with "is not a Node.js script".
// Replace pnpm's shim with a plain symlink straight to @tailwindcss/cli's
// entry point, which keeps its own `#!/usr/bin/env node` shebang intact.
import { createRequire } from "module";
import fs from "fs";
import { dirname, join } from "path";

const require = createRequire(import.meta.url);
const pkgPath = require.resolve("@tailwindcss/cli/package.json");
const pkg = JSON.parse(fs.readFileSync(pkgPath, "utf8"));
const target = join(dirname(pkgPath), pkg.bin.tailwindcss);

const binDir = join(process.cwd(), "node_modules", ".bin");
const linkPath = join(binDir, "tailwindcss");

fs.mkdirSync(binDir, { recursive: true });
fs.rmSync(linkPath, { force: true });
fs.symlinkSync(target, linkPath);
console.log(`Relinked node_modules/.bin/tailwindcss -> ${target}`);
