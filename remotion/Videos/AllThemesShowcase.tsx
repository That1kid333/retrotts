import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, interpolate } from "remotion";
import { AnimatedTerminal } from "./AnimatedTerminal";

const themes = [
  { key: "cyberpunk" as const, name: "CYBERPUNK" },
  { key: "matrix" as const, name: "MATRIX" },
  { key: "vaporwave" as const, name: "VAPORWAVE" },
  { key: "amber" as const, name: "AMBER TERMINAL" },
  { key: "neon" as const, name: "NEON CITY" },
  { key: "midnight" as const, name: "MIDNIGHT BLUE" },
];

export const AllThemesShowcase: React.FC = () => {
  const frame = useCurrentFrame();
  const durationPerTheme = 450; // 15 seconds at 30fps

  return (
    <AbsoluteFill style={{ backgroundColor: "#000000" }}>
      {themes.map((theme, index) => {
        const start = index * durationPerTheme;
        const end = start + durationPerTheme;

        // Fade in/out
        const opacity = interpolate(
          frame,
          [start, start + 30, end - 30, end],
          [0, 1, 1, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        return (
          <div
            key={theme.key}
            style={{
              position: "absolute",
              width: "100%",
              height: "100%",
              opacity,
            }}
          >
            {frame >= start && frame < end && (
              <Sequence from={start} durationInFrames={durationPerTheme}>
                <AnimatedTerminal theme={theme.key} />
              </Sequence>
            )}

            {/* Theme Name Overlay (first 90 frames of each theme) */}
            {frame >= start && frame < start + 90 && (
              <div
                style={{
                  position: "absolute",
                  top: "50%",
                  left: "50%",
                  transform: "translate(-50%, -50%)",
                  fontSize: "80px",
                  fontFamily: "monospace",
                  fontWeight: "bold",
                  color: "#FFFFFF",
                  textShadow: "0 0 40px #FFFFFF, 0 0 80px #FFFFFF",
                  zIndex: 1000,
                  opacity: interpolate(
                    frame,
                    [start, start + 15, start + 75, start + 90],
                    [0, 1, 1, 0]
                  ),
                  textAlign: "center",
                  padding: "40px",
                  background: "rgba(0, 0, 0, 0.8)",
                  border: "3px solid #FFFFFF",
                  borderRadius: "10px",
                }}
              >
                {theme.name}
              </div>
            )}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
