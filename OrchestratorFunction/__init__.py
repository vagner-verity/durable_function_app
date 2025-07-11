import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    outputs = []
    for name in ["Alice", "Bob", "Charlie"]:
        result = yield context.call_activity("HelloActivity", name)
        outputs.append(result)
    return outputs

main = df.Orchestrator.create(orchestrator_function)
