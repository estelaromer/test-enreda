<template>
  <div class="content-container">
    <h1>List of Notes:</h1>
    <br>
    <table id="users-table">
      <!-- Table Header Row -->
      <tr>
        <th>End Date</th>
        <th>Note</th>
        <th>User Email</th>
        <th>Task</th>
        <th>Tag</th>
      </tr>
      <!-- Table Elements (Rows) -->
      <tr v-for="note in notes" v-bind:key="note">
        <td>{{ (new Date(Date.parse(note.endDate))).toDateString() }}</td>
        <td>{{ note.note.substring(0,50) + '...' }}</td>
        <td>{{ note.userEmail }}</td>
        <td>{{ (note.task) ? 'Yes': 'No' }}</td>
        <td>{{ note.tag }}</td>
      </tr>
    </table>
    <br>
  </div>
</template>

<script>
export default {
  name: 'ListNotes',
  props: {
    notes: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
td, th {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #4CAF50;
  color: white;
}
</style>