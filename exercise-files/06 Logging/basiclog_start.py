# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging
import random

def main():    
    
    msg="%(message)s"
    time="%(asctime)s"
    s="%(lineno)d"
    fmtstr=f"{time}, line nr {s} : {msg}"
    # TODO: Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        format=fmtstr)

    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    # TODO: Output formatted strings to the log

    t=random.randint(1,100)

    logging.info(f"The number {t} is {'higher' if (t>50) else 'lower'} than 50\n")

if __name__ == "__main__":
    main()
