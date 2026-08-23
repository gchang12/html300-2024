import { ref } from 'vue'

export default function() {
  // Returns a function that toggles the border;
  const border = ref([]);
  const borderOn = ["border-success"];
  const toggleBorder = (e) => {
    const element = e.currentTarget;
    if (border.value[0] === borderOn[0]) {
      border.value = [];
      element.classList.remove(...borderOn);
    } else {
      border.value = borderOn;
      element.classList.add(...borderOn);
    }
    //alert("Hello from useBorder.js");
  }
  return {
    border,
    toggleBorder,
  };
}
