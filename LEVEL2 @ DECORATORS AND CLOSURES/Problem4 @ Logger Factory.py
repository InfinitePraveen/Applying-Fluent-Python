# Write a function `make_logger(prefix)` that returns a closure.
# The closure should print messages with the prefix.
def make_logger(prefix):
    
    def logger(message):
        """Print a message with the configured prefix."""
        print(f"[{prefix}] {message}")
    
    return logger

# Alternative version with more formatting options
def make_logger_advanced(prefix, separator=" ", bracket=True):

    if bracket:
        formatted_prefix = f"[{prefix}]"
    else:
        formatted_prefix = prefix
    
    def logger(message):
        """Print a message with the configured prefix."""
        print(f"{formatted_prefix}{separator}{message}")
    
    return logger

# Example usage
if __name__ == "__main__":
    # Basic usage
    error_log = make_logger("ERROR")
    warning_log = make_logger("WARNING")
    info_log = make_logger("INFO")
    
    # Use the loggers
    error_log("Disk full")
    warning_log("Low memory")
    info_log("User logged in")
    
    print()  # Empty line for separation
    
    # Using the advanced version
    debug_log = make_logger_advanced("DEBUG", separator=": ", bracket=False)
    critical_log = make_logger_advanced("CRITICAL", separator=" - ")
    
    debug_log("Connection established")
    critical_log("System crash imminent")
    
    print()  # Empty line
    error_log("Another error occurred")
    info_log("Process completed")
    
    print(f"\nClosure's captured variables: {error_log.__closure__[0].cell_contents}")

# Example:
# error_log = make_logger("ERROR")
# error_log("Disk full") # Prints: [ERROR] Disk full