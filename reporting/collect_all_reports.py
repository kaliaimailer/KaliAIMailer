from ScreenshotModule import take_screenshot
import glob
import os

def collect_reports():
    """Collects all necessary reports and returns a list of file paths."""
    reports = []
    
    # Take a screenshot and add it to the reports list
    screenshot_file = take_screenshot()
    reports.append(screenshot_file)
    
    # Collect all .log files from the logs directory
    log_files_directory = 'C:/KaliAIMailer/logs/'
    log_files = glob.glob(os.path.join(log_files_directory, '*.txt'))
    reports.extend(log_files)
    
    # Optionally, filter log files by modification time or other criteria here
    
    return reports
