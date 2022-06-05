<template>
  <div>
    <vue-tree
      style="width: 100%; height: 300px; border: 1px solid gray"
      :dataset="sampleData"
      :config="treeConfig"
    >
      <template v-slot:node="{ node, collapsed }">
        <span
          class="tree-node"
          :style="{
            border: collapsed ? '2px solid grey' : '',
            borderRadius: '50%',
          }"
          >{{ node.value }}</span
        >
      </template>
    </vue-tree>
  </div>
</template>
<script>
import VueTree from "@ssthouse/vue3-tree-chart";
import "@ssthouse/vue3-tree-chart/dist/vue3-tree-chart.css";

export default {
  components: { VueTree },
  data() {
    return {
      sampleData: {
        value: "Мать Кайрата",
        children: [
          { value: "Кайрат", children: [{ value: "НК" }, { value: "Пизда" }] },
          { value: "Брат Кайрата" },
        ],
      },
      treeConfig: { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 },
    };
  },
};

// let sampleData =  {
//   value: "1",
//   children: [
//     { value: "2", children: [{ value: "4" }, { value: "5" }] },
//     { value: "3" },
//   ],
// };
// let treeConfig = { nodeWidth: 120, nodeHeight: 80, levelHeight: 200 };
</script>


<style>
#TreeVII {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: right;
  color: #2d6328;
  margin-top: 2px;
  box-shadow:  0 7px 6px rgba(0,0,0,0.3);;
}
.tree-node {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-color: rgba(233, 184, 207, 0.836);
  text-align: right;
  line-height: 28px;
}
</style>
