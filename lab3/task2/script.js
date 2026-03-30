const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

// Add task
addTaskBtn.addEventListener("click", function() {
    const taskText = taskInput.value.trim();

    if (taskText === "") return;

    // Create elements
    const li = document.createElement("li");

    const taskLeft = document.createElement("div");
    taskLeft.className = "task-left";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const span = document.createElement("span");
    span.textContent = taskText;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "delete-btn";

    // Append elements
    taskLeft.appendChild(checkbox);
    taskLeft.appendChild(span);

    li.appendChild(taskLeft);
    li.appendChild(deleteBtn);

    taskList.appendChild(li);

    taskInput.value = "";

    // Mark as done
    checkbox.addEventListener("change", function() {
        if (checkbox.checked) {
            span.classList.add("done");
        } else {
            span.classList.remove("done");
        }
    });

    // Delete task
    deleteBtn.addEventListener("click", function() {
        taskList.removeChild(li);
    });
});