import React from "react";
import { AnimatedTerminal } from "./AnimatedTerminal";

export const NeonTheme: React.FC = () => {
  return (
    <AnimatedTerminal
      theme="neon"
      demoText="Bright lights... big city... rainbow colors everywhere... maximum visual impact... speech-to-text overload!"
    />
  );
};
