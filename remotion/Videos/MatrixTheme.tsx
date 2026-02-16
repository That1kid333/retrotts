import React from "react";
import { AnimatedTerminal } from "./AnimatedTerminal";

export const MatrixTheme: React.FC = () => {
  return (
    <AnimatedTerminal
      theme="matrix"
      demoText="Wake up Neo... the Matrix has you... now you can type what you say in the ultimate hacker aesthetic!"
    />
  );
};
