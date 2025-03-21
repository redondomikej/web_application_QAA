import os
import time
from utils.webdriver_manager import get_driver
from utils.screenshot import capture_screenshot
from utils.video_recorder import VideoRecorder  # ✅ Import VideoRecorder

def before_all(context):
    context.browser = "chrome"
    context.incognito = False    
    context.headless = False    
    context.additional_args = ["--disable-popup-blocking"]

    context.driver = get_driver(
        browser=context.browser,
        incognito=context.incognito,
        headless=context.headless,
        additional_args=context.additional_args
    )

def before_scenario(context, scenario):
    """Start video recording before each scenario."""
    if not hasattr(context, "driver") or context.driver is None:
        raise AttributeError("context.driver is not initialized. Make sure to start the WebDriver in before_all().")

    scenario_name = scenario.name.replace(" ", "_")
    context.video_recorder = VideoRecorder(context.driver, scenario_name)
    context.video_recorder.start_recording()  # ✅ Start recording

def after_step(context, step):
    """Capture frames after each step."""
    if hasattr(context, "video_recorder"):
        print(f"🎥 Capturing frame for step: {step.name}")  # 🔍 Debug log
        context.video_recorder.record_frame()

    if step.status == "failed":
        print(f"❌ Step failed: {step.name}")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        scenario_name = f"{context.scenario.name.replace(' ', '_')}_{timestamp}"
        capture_screenshot(context.driver, scenario_name)

def after_scenario(context, scenario):
    """Stop video recording after scenario."""
    if hasattr(context, "video_recorder"):
        scenario_failed = scenario.status == "failed"  # ✅ Determine if scenario failed
        print(f"🛑 Stopping recording for scenario: {scenario.name}, Failed: {scenario_failed}")  # 🔍 Debug log
        context.video_recorder.stop_recording(scenario_failed)

def after_all(context):
    """Quit WebDriver after all scenarios."""
    if hasattr(context, "driver"):
        context.driver.quit()
        print("🚀 WebDriver closed.")
import os
import time
from utils.webdriver_manager import get_driver
from utils.screenshot import capture_screenshot
from utils.video_recorder import VideoRecorder  # ✅ Import VideoRecorder

def before_all(context):
    context.browser = "chrome"
    context.incognito = False    
    context.headless = False    
    context.additional_args = ["--disable-popup-blocking"]

    context.driver = get_driver(
        browser=context.browser,
        incognito=context.incognito,
        headless=context.headless,
        additional_args=context.additional_args
    )

def before_scenario(context, scenario):
    """Start video recording before each scenario."""
    if not hasattr(context, "driver") or context.driver is None:
        raise AttributeError("context.driver is not initialized. Make sure to start the WebDriver in before_all().")

    scenario_name = scenario.name.replace(" ", "_")
    context.video_recorder = VideoRecorder(context.driver, scenario_name)
    context.video_recorder.start_recording()  # ✅ Start recording

def after_step(context, step):
    """Capture frames after each step."""
    if hasattr(context, "video_recorder"):
        print(f"🎥 Capturing frame for step: {step.name}")  # 🔍 Debug log
        context.video_recorder.record_frame()

    if step.status == "failed":
        print(f"❌ Step failed: {step.name}")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        scenario_name = f"{context.scenario.name.replace(' ', '_')}_{timestamp}"
        capture_screenshot(context.driver, scenario_name)

def after_scenario(context, scenario):
    """Stop video recording after scenario."""
    if hasattr(context, "video_recorder"):
        scenario_failed = scenario.status == "failed"  # ✅ Determine if scenario failed
        print(f"🛑 Stopping recording for scenario: {scenario.name}, Failed: {scenario_failed}")  # 🔍 Debug log
        context.video_recorder.stop_recording(scenario_failed)

def after_all(context):
    """Quit WebDriver after all scenarios."""
    if hasattr(context, "driver"):
        context.driver.quit()
        print("🚀 WebDriver closed.")
