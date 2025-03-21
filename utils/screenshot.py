import os

def capture_screenshot(driver, scenario_name):
    """Captures a screenshot and saves it in the 'test_evidence/screenshots' directory."""
    
    screenshots_dir = "test_evidence/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)  # Ensure folder exists

    filepath = os.path.join(screenshots_dir, f"{scenario_name}.png")

    print(f"📂 Screenshot directory: {screenshots_dir}")  # Debug folder existence
    print(f"📸 Saving screenshot to: {filepath}")  # Verify filename and path

    try:
        driver.save_screenshot(filepath)
        print(f"✅ Screenshot saved successfully: {filepath}")  # Confirm if it saves
    except Exception as e:
        print(f"❌ ERROR capturing screenshot: {e}")  # Catch errors
