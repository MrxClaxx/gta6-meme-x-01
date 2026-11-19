// gta6-meme-x-01 entrypoint (Node 22, standard library only).
// The entry is the X post itself: the meme was made by the agent, posted on X
// from a public account, and POST.json at the repository root names the post.
// This program only hands that address to the gate by copying POST.json
// from the repository root into the output directory.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

// The grader mounts the repository at /bot and collects results from
// /output; both can be overridden for a local run. The gate reads the
// copied POST.json to find the post on X, so a failed copy fails the run.
const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(OUTPUT_DIR, { recursive: true });

try {
  copyFileSync(join(BOT_DIR, "POST.json"), join(OUTPUT_DIR, "POST.json"));
  console.log(`POST.json copied to ${join(OUTPUT_DIR, "POST.json")}`);
} catch (error) {
  console.error(
    `Could not copy POST.json from ${BOT_DIR}: ${(error as Error).message}`,
  );
  process.exit(1);
}

// Fail fast if the copied file is not a JSON object with a url string,
// so a broken POST.json never reaches the gate silently.
try {
  const posted = JSON.parse(
    readFileSync(join(OUTPUT_DIR, "POST.json"), "utf8"),
  ) as unknown;
  if (
    typeof posted !== "object" ||
    posted === null ||
    typeof (posted as { url?: unknown }).url !== "string"
  ) {
    throw new Error("POST.json has no url string");
  }
} catch (error) {
  console.error(`POST.json is not usable: ${(error as Error).message}`);
  process.exit(1);
}
