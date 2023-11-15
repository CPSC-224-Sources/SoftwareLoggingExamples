import java.io.IOException;
import java.util.logging.ConsoleHandler;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LoggingExample {

    public static void main(String[] args) {
        // Create logger
        Logger logger = Logger.getLogger(LoggingExample.class.getName());

        // Set the logging level to INFO
        logger.setLevel(Level.INFO);

        try {
            // Create a file handler and set its formatter
            FileHandler fileHandler = new FileHandler("prog.log");
            fileHandler.setFormatter(new SimpleFormatter());

            // Add the file handler to the logger
            logger.addHandler(fileHandler);

            // Log messages with different levels
            logger.severe("This is a SEVERE message");
            logger.warning("This is a WARNING message");
            logger.info("This is an INFO message");
            logger.config("This is a CONFIG message");
            logger.fine("This is a FINE message (DEBUG)");
            logger.finer("This is a FINER message");
            logger.finest("This is a FINEST message");

        } catch (IOException e) {
            e.printStackTrace();
        }

        // Log to STDOUT (console)
        ConsoleHandler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);
        logger.addHandler(consoleHandler);

        // Log additional messages to STDOUT
        logger.info("This is another INFO message");
        logger.warning("This is another WARNING message");
        logger.fine("This is another FINE message (DEBUG)");
    }
}
