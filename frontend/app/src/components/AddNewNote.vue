<template>
  <div class="content-container">
    <h1>Add a New Note:</h1>
    <br>
    <div class="add-note-input">
        <label for="newEndDate">EndDate:</label>
        <input
            type="datetime-local"
            ref="input"
            id="newEndDate" 
            value="note.endDate"
            v-model="note.endDate"
        >
        <br>
        <span>Note:</span>
        <p style="white-space: pre-line;">{{ note.note }}</p>
        <br>
        <textarea v-model="note.note"></textarea>
        <br>
        <select v-model="note.userEmail">
        <option disabled value="">Seleccione un usuario</option>
        <option>user1@example.com</option>
        <option>user2@example.com</option>
        <option>user3@example.com</option>
        </select>
        <span>Seleccionado: {{ note.userEmail }}</span>
        <br>
        <label for="newTask">Task?:</label>
        <input type="checkbox" id="newTask" v-model="note.task">
        <br>
        <label for="newTag">Tag:</label>
        <input type="text" id="newTag" v-model="note.tag">
        <br>
        <button type="submit" v-on:click="addNewUser">Add Note</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'AddNewUser',
    data () {
        return {
            note: {
                endDate: new Date(),
                note: '',
                userEmail: '',
                task: false,
                tag: ''
            }
        }
    },
    methods: {
        addNewUser() {
            this.$emit('create-note', this.note);

            // Clear the variables used for reading in the new user's info
            this.note.endDate = new Date();
            this.note.note = '';
            this.note.userEmail = '';
            this.note.task = false;
            this.note.tag = ''
        }
    }
}
</script>

<style scoped>
.content-container {
  margin: auto;
}

.add-note-input label {
  float: left;
  width: 25%;
  margin-top: 6px;
  padding: 4px;
}

.add-note-input input {
  float: left;
  width: 75%;
  margin-top: 6px;
  padding: 4px;
  font-size: 1em;
}

.add-note-input input[type=text]:focus {
  border-color:#333;
}

.add-note-input input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>