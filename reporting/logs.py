from datetime import datetime, timedelta

# Current time
now = datetime.now()

# Filter log files modified in the last 24 hours
recent_log_files = [file for file in log_files if datetime.fromtimestamp(os.path.getmtime(file)) > now - timedelta(days=1)]

# Use recent_log_files instead of log_files if filtering is needed
reports.extend(recent_log_files)
