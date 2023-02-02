<script setup>
import { ref, shallowRef, computed, watch, nextTick } from "vue";
import Chart from "chart.js/auto";

const weight = ref([]);

const weightChartEl = ref(null);

const weightChart = shallowRef(null);
</script>

<template>
  <h1>Hello</h1>
</template>

<style scoped></style>
