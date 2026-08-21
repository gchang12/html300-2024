/* TODO:
  ( ) For the image page, convert the image markup into a separate component in its own file, be sure to import it into the corresponding 'page' component
  ( ) The image component should have props for at least the image src, alt, & title attributes, use prop validation.
  ( ) Creation and use of slot for header component
  (X) Create a mixin for the image component that should toggle on/off a border around the image on click, apply the mixin to the image component.
  ( ) Don't forget to add comments to your code explaining Bootstrap classes you added and your VUE code.
*/

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
