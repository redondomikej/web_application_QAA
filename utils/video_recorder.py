import os
import cv2
import numpy as np
import mss
from datetime import datetime

class VideoRecorder:
    def __init__(self, driver, scenario_name):
        """Initialize video recording for a scenario."""
        self.driver = driver
        self.scenario_name = scenario_name.replace(" ", "_")
        self.recording = False
        self.video_writer = None
        self.sct = mss.mss()

        # ✅ Ensure test_evidence/videos folder exists
        self.video_dir = "test_evidence/videos"
        os.makedirs(self.video_dir, exist_ok=True)

        # 🎥 Create a video file path with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.video_path = os.path.join(self.video_dir, f"{self.scenario_name}_{timestamp}.avi")

    def start_recording(self):
        """Start video recording."""
        try:
            # Get browser window size
            window_rect = self.driver.get_window_rect()
            x, y, width, height = window_rect["x"], window_rect["y"], window_rect["width"], window_rect["height"]

            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            self.video_writer = cv2.VideoWriter(self.video_path, fourcc, 20.0, (width, height))
            self.recording = True
            print(f"🎥 Recording started: {self.video_path}")

        except Exception as e:
            print(f"❌ Error starting video recording: {e}")

    def record_frame(self):
        """Capture and save a frame."""
        if self.recording:
            try:
                window_rect = self.driver.get_window_rect()
                x, y, width, height = window_rect["x"], window_rect["y"], window_rect["width"], window_rect["height"]

                screenshot = self.sct.grab({"left": x, "top": y, "width": width, "height": height})
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convert format
                self.video_writer.write(frame)

            except Exception as e:
                print(f"❌ Error recording frame: {e}")

    def stop_recording(self, scenario_failed):
        """Stop video recording and delete if scenario passed."""
        if self.recording:
            self.video_writer.release()
            self.recording = False

            if scenario_failed:
                print(f"✅ Video saved: {self.video_path}")
            else:
                try:
                    os.remove(self.video_path)
                    print(f"🗑️ Deleted video (Scenario Passed): {self.video_path}")
                except Exception as e:
                    print(f"❌ Error deleting video: {e}")
