// Stream Task 
public class StreamClass implements StreamTask{
    public void process(IncomingMessageEnvelope envelope,
                        MessageCollector collector,
                        TaskCoordinator coordinator) {
    }
}

// Samza instantiates when the job is run
task.class=com.example.samza.StreamClass

//



