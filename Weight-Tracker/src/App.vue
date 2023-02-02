<script setup>
import { ref, shallowRef, computed, watch, nextTick } from "vue";
import Chart from "chart.js/auto";

const weight = ref([]);

const weightChartEl = ref(null);

const weightChart = shallowRef(null);

const weightInput = ref(60.0);

const currentWeight = computed(
  () => weight.value.sort((a, b) => b.date - a.date)[0] || { weight: 0 }
);

const addWeight = () => {
  weight.value.push({
    weight: weightInput.value,
    date: new Date().getTime(),
  });
};
</script>

<template>
  <h1>Hello</h1>
</template>

<style scoped></style>
