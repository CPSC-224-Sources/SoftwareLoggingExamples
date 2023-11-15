import logging
import sys

def setup_logger(isDebug=False, isVerbose=False):
    # Create logger
    logger = logging.getLogger(__name__)
    if(isDebug):
        logger.setLevel(logging.DEBUG)   # Can set log level any time
    elif(isVerbose):
        logger.setLevel(logging.INFO)   # Can set log level any time
    else:
        logger.setLevel(logging.WARNING)   # Can set log level any time

    # Create file handler and set its formatter
    file_handler = logging.FileHandler("prog.log")
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Create console handler and set its formatter
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def main():
    isDebug = False
    isVerbose = False
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-d"):
            isDebug = True
        if(sys.argv[1] == "-v"):
            isVerbose = True
        
    # Set up logger
    logger = setup_logger(isDebug=isDebug, isVerbose=isVerbose)

    # Log messages with different levels
    logger.critical("This is a CRITICAL (we die) message")
    logger.error("This is a ERROR message")
    logger.warning("This is a WARNING message")
    logger.info("This is an INFO message")
    logger.debug("This is a DEBUG message")

    # Log additional messages to STDOUT
    logger.info("This is another INFO message")
    logger.warning("This is another WARNING message")

if __name__ == "__main__":
    main()

