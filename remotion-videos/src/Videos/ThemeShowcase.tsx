import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, Sequence } from "remotion";

const themes = [
  { name: "CYBERPUNK", color: "#00FFFF", accent: "#FF00FF", bg: "#000000" },
  { name: "MATRIX", color: "#00FF00", accent: "#00FF00", bg: "#000000" },
  { name: "VAPORWAVE", color: "#FF00FF", accent: "#00FFFF", bg: "#000000" },
  { name: "AMBER", color: "#FFAA00", accent: "#FFFF00", bg: "#000000" },
  { name: "NEON CITY", color: "#FF0000", accent: "#00FFFF", bg: "#000000" },
  { name: "MIDNIGHT", color: "#0099FF", accent: "#00DDFF", bg: "#000000" },
];

const ThemeSection: React.FC<{ theme: typeof themes[0]; startFrame: number }> = ({ theme, startFrame }) => {
  const frame = useCurrentFrame();
  const relativeFrame = frame - startFrame;

  // Fade in/out
  const opacity = interpolate(
    relativeFrame,
    [0, 15, 135, 150],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Scale animation
  const scale = interpolate(
    relativeFrame,
    [0, 30, 120, 150],
    [0.8, 1, 1, 1.1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Glow animation
  const glow = interpolate(
    relativeFrame,
    [0, 75, 150],
    [0, 50, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <AbsoluteFill
      style={{
        backgroundColor: theme.bg,
        opacity,
        transform: `scale(${scale})`,
      }}
    >
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          fontFamily: "monospace",
        }}
      >
        {/* Theme Name */}
        <h1
          style={{
            fontSize: 180,
            color: theme.color,
            textShadow: `0 0 ${glow}px ${theme.color}, 0 0 ${glow * 2}px ${theme.accent}`,
            marginBottom: 60,
            letterSpacing: 15,
          }}
        >
          {theme.name}
        </h1>

        {/* Simulated VU Meter */}
        <div
          style={{
            width: 1200,
            height: 80,
            border: `5px solid ${theme.color}`,
            borderRadius: 15,
            padding: 10,
            boxShadow: `0 0 30px ${theme.color}`,
          }}
        >
          <div
            style={{
              width: `${interpolate(relativeFrame % 60, [0, 60], [10, 90])}%`,
              height: "100%",
              background: `linear-gradient(90deg, ${theme.color}, ${theme.accent})`,
              borderRadius: 5,
              transition: "width 0.3s",
            }}
          />
        </div>

        {/* Status Text */}
        <p
          style={{
            fontSize: 72,
            color: theme.accent,
            marginTop: 60,
            textShadow: `0 0 15px ${theme.accent}`,
            fontWeight: "bold",
          }}
        >
          {relativeFrame < 60 ? "● READY" : relativeFrame < 120 ? "● RECORDING" : "✓ COMPLETE"}
        </p>
      </div>
    </AbsoluteFill>
  );
};

export const ThemeShowcase: React.FC = () => {
  const { durationInFrames } = useVideoConfig();
  const framesPerTheme = durationInFrames / themes.length;

  return (
    <AbsoluteFill style={{ backgroundColor: "#000000" }}>
      {themes.map((theme, index) => (
        <Sequence
          key={theme.name}
          from={index * framesPerTheme}
          durationInFrames={framesPerTheme}
        >
          <ThemeSection theme={theme} startFrame={index * framesPerTheme} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
