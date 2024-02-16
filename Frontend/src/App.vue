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
        console.log("URL extraite :", src);
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
  <div>
    <input type="text" v-model="text" />
    <button @click="getTTS">TTS</button>
  </div>
</template>

<style scoped></style>
