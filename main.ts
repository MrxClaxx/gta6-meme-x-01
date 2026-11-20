// Round-2 entry for gta6-meme-x-01: "Vice City parking violation" meme.
// The entry is the X post itself; this program only copies the post file
// (POST.json) and the meme picture into the output directory, as the
// competition's rules describe. Nothing it writes is judged.
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const postPath = join(here, "POST.json");
// Fail fast if the post file is not valid JSON instead of copying a bad file.
const post = JSON.parse(readFileSync(postPath, "utf8")) as { url?: unknown };
if (typeof post.url !== "string" || post.url.length === 0) {
  throw new Error("POST.json must hold a non-empty url string");
}
copyFileSync(postPath, join(outDir, "POST.json"));
copyFileSync(join(here, "meme.png"), join(outDir, "meme.png"));
console.log(`Wrote POST.json and meme.png to ${outDir}`);
