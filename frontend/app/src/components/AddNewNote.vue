<template>
  <div class="content-container">
    <h1>Add a New Note:</h1>
    <br>
    <div class="add-note-input">
      <div class="form-elem-wrapper">
        <label for="newEndDate">End Date:</label>
        <input
            type="datetime-local"
            ref="input"
            id="newEndDate" 
            value="note.endDate"
            v-model="note.endDate"
        >
      </div>
      <div class="form-elem-wrapper">
        <label for="newNote">Note:</label>
        <textarea v-model="note.note"></textarea>
      </div>
      <div class="form-elem-wrapper">
        <label for="newAttachedFile">File:</label>
        <input type="file" id="attachedFile" ref="file" v-on:change="handleFileUpload()"/>
      </div>
      <div class="form-elem-wrapper">
          <label for="newUserEmail">User:</label>
          <select v-model="note.userEmail">
          <option disabled value="">Select a user</option>
          <option v-for="user in users" v-bind:key="user">{{ user.email }}</option>
        </select>
      </div>
      <div class="form-elem-wrapper">
        <label for="newTask">Task?:</label>
        <input type="checkbox" id="newTask" v-model="note.task">
      </div>
      <div class="form-elem-wrapper">
        <label for="newTag">Tag:</label>
        <input type="text" id="newTag" v-model="note.tag">
      </div>
      <div class="form-elem-wrapper">
        <button type="submit" v-on:click="addNewUser">Add Note</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddNewUser',
  props:{
    users: Array
  },
  data () {
      return {
          note: {
              endDate: new Date(),
              note: '',
              attachedFile: null,
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
        this.note.attachedFile = null;
        this.note.userEmail = '';
        this.note.task = false;
        this.note.tag = '';
        this.$refs.file.value= '' ;
      },
      handleFileUpload(){
        this.note.attachedFile = this.$refs.file.files[0];
      }
  }
}
</script>

<style scoped>
.content-container {
  margin: auto;
  width: 400px;
}
.add-note-input .form-elem-wrapper {
  margin: 1em;
}

.add-note-input .form-elem-wrapper label {
  float: left;
  width: 30%;
}

.add-note-input .form-elem-wrapper textarea {
  width: 100%;
  margin: 1em;
}

.add-note-input .form-elem-wrapper input[type=file] {
  margin: 1em;
}

.add-note-input .form-elem-wrapper select {
  width: 100%;
  margin: 1em;
  padding: 0.5em;
}

.add-note-input .form-elem-wrapper input[type=text] {
  width: 65%;
}

.add-note-input .form-elem-wrapper button[type=submit] {
  width: 100%;
  padding: 1em;
  background-color: #4CAF50;
  cursor: pointer;
}
/*.add-note-input label {
  float: left;
  width: 50%;
  margin-top: 6px;
  padding: 4px;
}

.add-note-input input {
  float: left;
  width: 50%;
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
} */
</style>