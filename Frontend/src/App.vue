<script setup>
import axios from "axios";
import { ref } from "vue";

const text = ref("");

const getTTS = () => {
  axios
    .get("http://127.0.0.1:5000/" + text.value)
    .then((res) => {
      var match = res.data.match(/src="([^"]+)"/);

      if (match && match.length > 1) {
        var src = match[1];
        const audio = new Audio(src);
        audio.play();
      } else {
        console.log("Aucune URL trouvée dans la chaîne.");
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<template>
  <div class="main">
    <h1>Text to Speech</h1>
    <h3>INFO 904</h3>
    <p>Entrez le texte que vous souhaitez lire :</p>
    <textarea type="text" v-model="text" />
    <button @click="getTTS">Lire le TTS</button>
  </div>
  <footer>
    <p>Cosson Méwen, Jonathan Dumont, Rakotoanosy Ewan, Guigue Billon Arnaud</p>
  </footer>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  margin-bottom: 0;
}

h3 {
  margin-top: 0;
}

textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  font-size: 17px;
  font-family: "Arial", sans-serif;
  color: #333;
  transition: 0.5s;

  &:focus {
    border: 3px solid #555;
  }

  &:hover {
    border: 3px solid #555;
  }

  &:active {
    border: 3px solid #555;
  }
}

button {
  width: 100%;
  height: 40px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

button:active {
  background-color: #3e8e41;
}

footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  background-color: #f8f8f8;
  padding: 10px;
  border-top: 1px solid #e7e7e7;
  color: #333;
  font-size: 12px;
  font-family: "Arial", sans-serif;
  color: #333;
  transition: 0.5s;
}
</style>
