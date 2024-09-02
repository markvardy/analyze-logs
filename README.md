# analyze-logs
Work experience code

The Ask:
Write a script that
1. Take in a CSV file of raw analytics records.
1. Split it into separate files depending on API name
1. For each file
   - The latency_info field is a json object detailing the time taken for each stage of the API. Transform this field into the following example. Remembering to ensure that duration is duration not the start time. 
    `[  {  'name' :  'policyname' ,  'Duration' : '1000' } , {  'name' :  'policyname2' ,  'Duration' : '15000' }, {  'name' :  'policyname3' ,  'Duration' : '10' } ]`
   - Produce a graph similar to the below  with a sensible name.
