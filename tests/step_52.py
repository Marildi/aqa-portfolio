# Step 53: Visual testing — screenshots, expect(page).to_have_screenshot()
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import Page

BASELINE_DIR = Path("tests/baselines")
BASELINE_DIR.mkdir(parents=True, exist_ok=True)


def test_saucedemo_login_visual(page: Page):
    page.goto("https://www.saucedemo.com")
    # page.evaluate("document.querySelector('[data-test=\"login-button\"]').style.backgroundColor = 'red'")   # force a visible change
    baseline_path = BASELINE_DIR / "saucedemo_login.png"
    current_path = BASELINE_DIR / "saucedemo_login_current.png"

    page.screenshot(path=current_path)

    if not baseline_path.exists():
        # first run - save current as the new baseline
        current_path.rename(baseline_path)
        print("Baseline created - nothing to compare yet")
        return

    baseline_img = Image.open(baseline_path).convert("RGB")
    current_img = Image.open(current_path).convert("RGB")

    if baseline_img.size != current_img.size:
        raise AssertionError(
            f"Image size mismatch: baseline={baseline_img.size}, current={current_img.size}"
        )

    diff = ImageChops.difference(baseline_img, current_img)
    bbox = (
        diff.getbbox()
    )  # returns None if images are identical, otherwise the bounding box of differences

    if bbox is not None:
        diff_path = BASELINE_DIR / "saucedemo_login_diff.png"
        diff.save(diff_path)
        raise AssertionError(
            f"Visual difference detected! Diff region: {bbox}. See {diff_path}"
        )

    print("Visual comparison passed - no differences detected")
