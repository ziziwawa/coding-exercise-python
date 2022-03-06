# coding-exercise-python

### Instructions

Execute the commands below to start the app.

   ```sh
   docker-compose up
   ```

Execute the commands below to get the tasks.

   ```sh
   curl -X GET http://localhost:5000/tasks
   ```
   
Execute the commands below to add a task.

   ```sh
   curl -X POST -H "Content-Type: application/json" -d '{"name": "Go Shopping"}' http://localhost:5000/tasks
   ```
   
Execute the commands below to update a task no 1.

   ```sh
   curl -X PUT -H "Content-Type: application/json" -d '{"name": "Modify a task", "status": 1, "id": 1}' http://localhost:5000/tasks/1
   ```
   
Execute the commands below to delete a task.

   ```sh
   curl -X DELETE http://localhost:5000/tasks/2
   ```
