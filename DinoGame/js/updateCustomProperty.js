function getCustomProperty(elem, prop) {
  return parseFloat(getComputedStyle(elem).getPropertyValue(prop)) || 0;
}

function setCustomProperty(elem, prop, value) {
  $(elem).css(prop, value);
}

function increamentCustomProperty(elem, prop, inc) {
  setCustomProperty(elem, prop, getCustomProperty(elem, prop) + inc);
}

export { getCustomProperty, setCustomProperty, increamentCustomProperty };
