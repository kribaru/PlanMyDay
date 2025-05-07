async function fetchPlan() {
    const dateInput = document.getElementById("dateInput").value;
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";
  
    if (!dateInput) {
      resultsDiv.innerHTML = "<p>Please select a date.</p>";
      return;
    }
  
    try {
      const response = await fetch(`http://localhost:5000/plan/${dateInput}`);
      const data = await response.json();
  
      if (data.plannedEvents.length === 0) {
        resultsDiv.innerHTML = "<p>No events found for this date.</p>";
        return;
      }
  
      const list = document.createElement("ul");
  
      data.plannedEvents.forEach(event => {
        const item = document.createElement("li");
        item.innerHTML = `
          <strong>${event.title}</strong><br>
          Type: ${event.type}<br>
          Time: ${event.startTime} - ${event.endTime}<br>
          Prep: ${event.prepItems.join(", ")}
        `;
        list.appendChild(item);
      });
  
      resultsDiv.appendChild(list);
    } catch (err) {
      console.error(err);
      resultsDiv.innerHTML = "<p>Error fetching plan.</p>";
    }
  }
  