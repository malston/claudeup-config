const { chromium } = require("playwright");

const TARGET_URL = "http://localhost:3001";

const MOCK_CORRELATIONS = {
  credit_tech: Array.from({ length: 79 }, (_, i) => ({
    time: `2026-01-${String(i + 1).padStart(2, "0")}`,
    value: 0.3 + Math.sin(i / 10) * 0.2,
  })),
  credit_energy: Array.from({ length: 79 }, (_, i) => ({
    time: `2026-01-${String(i + 1).padStart(2, "0")}`,
    value: 0.1 + Math.cos(i / 10) * 0.15,
  })),
  tech_energy: Array.from({ length: 79 }, (_, i) => ({
    time: `2026-01-${String(i + 1).padStart(2, "0")}`,
    value: 0.2 + Math.sin(i / 8) * 0.1,
  })),
  max_current: {
    pair: "credit_tech",
    value: 0.623,
    above_threshold: true,
  },
};

const MOCK_SCORES = {
  composite: { score: 62, level: "HIGH", color: "#f97316" },
  domains: {
    private_credit: { score: 68, level: "HIGH", weight: 0.3, color: "#f97316" },
    ai_concentration: {
      score: 45,
      level: "ELEVATED",
      weight: 0.2,
      color: "#eab308",
    },
    energy_geo: { score: 72, level: "HIGH", weight: 0.25, color: "#f97316" },
    contagion: { score: 58, level: "HIGH", weight: 0.25, color: "#f97316" },
  },
  updated_at: "2026-03-20T15:00:00Z",
};

(async () => {
  const browser = await chromium.launch({ headless: false, slowMo: 200 });
  const page = await browser.newPage();
  let passed = 0;
  let failed = 0;

  function assert(condition, msg) {
    if (condition) {
      console.log(`  PASS: ${msg}`);
      passed++;
    } else {
      console.error(`  FAIL: ${msg}`);
      failed++;
    }
  }

  // Mock all API routes with a single handler
  await page.route("**/api/risk/**", (route) => {
    const url = route.request().url();
    if (url.includes("/api/risk/correlations")) {
      return route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify(MOCK_CORRELATIONS),
      });
    }
    if (url.includes("/api/risk/scores")) {
      return route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify(MOCK_SCORES),
      });
    }
    if (url.includes("/api/risk/freshness")) {
      return route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ tickers: {} }),
      });
    }
    if (url.includes("/api/risk/health")) {
      return route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ sources: [] }),
      });
    }
    // Default: return empty array for list endpoints
    return route.fulfill({
      status: 200,
      contentType: "application/json",
      body: "[]",
    });
  });

  await page.goto(TARGET_URL, { waitUntil: "networkidle" });

  // ---- Test 1: contagion-threshold-label testid is discoverable ----
  console.log(
    "\n--- Test 1: CONTAGION THRESHOLD label discoverable by testid ---",
  );

  const label = page.locator('[data-testid="contagion-threshold-label"]');
  try {
    await label.waitFor({ state: "attached", timeout: 10000 });
    assert(true, "contagion-threshold-label testid found");

    const text = await label.textContent();
    assert(
      text.includes("CONTAGION THRESHOLD"),
      `label text is "CONTAGION THRESHOLD" (got: "${text}")`,
    );
  } catch {
    assert(false, "contagion-threshold-label testid found (timed out)");
  }

  // ---- Test 2: Label is discoverable by Playwright text selector ----
  console.log("\n--- Test 2: Label discoverable by text selector ---");

  const textLabel = page.locator("text=CONTAGION THRESHOLD");
  const textCount = await textLabel.count();
  assert(
    textCount > 0,
    `Playwright text selector finds "CONTAGION THRESHOLD" (count: ${textCount})`,
  );

  // ---- Test 3: Correlation chart renders with data ----
  console.log("\n--- Test 3: Correlation chart renders correctly ---");

  const chartPanel = page.locator('[data-testid="correlation-chart-panel"]');
  assert(await chartPanel.isVisible(), "correlation-chart-panel visible");

  const rhoValue = page.locator('[data-testid="correlation-rho-value"]');
  try {
    await rhoValue.waitFor({ state: "visible", timeout: 10000 });
    const rhoText = await rhoValue.textContent();
    assert(rhoText.includes("0.623"), `rho value is 0.623 (got: "${rhoText}")`);
  } catch {
    assert(false, "rho value visible (timed out)");
  }

  await page.screenshot({
    path: "/tmp/contagion-threshold-label.png",
    fullPage: true,
  });
  console.log("  Screenshot: /tmp/contagion-threshold-label.png");

  // ---- Summary ----
  console.log(`\n=== Results: ${passed} passed, ${failed} failed ===`);

  await browser.close();

  if (failed > 0) process.exit(1);
})();
