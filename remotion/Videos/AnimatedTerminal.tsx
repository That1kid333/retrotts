import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, spring, useVideoConfig } from "remotion";

interface Theme {
  name: string;
  primary: string;
  secondary: string;
  accent: string;
  dim: string;
  saying: string;
}

const themes: Record<string, Theme> = {
  cyberpunk: {
    name: "RETRO TTS",
    primary: "#00FFFF",
    secondary: "#FF00FF",
    accent: "#00FF00",
    dim: "#666666",
    saying: "Welcome to the future of speech-to-text",
  },
  matrix: {
    name: "RETRO TTS",
    primary: "#00FF00",
    secondary: "#00FF00",
    accent: "#00FF00",
    dim: "#006600",
    saying: "The Matrix has you... now type what you say",
  },
  vaporwave: {
    name: "RETRO TTS",
    primary: "#FF00FF",
    secondary: "#00FFFF",
    accent: "#FF00FF",
    dim: "#663366",
    saying: "A E S T H E T I C  speech recognition vibes",
  },
  amber: {
    name: "RETRO TTS",
    primary: "#FFAA00",
    secondary: "#FFFF00",
    accent: "#FFCC00",
    dim: "#664400",
    saying: "Classic computing meets modern speech tech",
  },
  neon: {
    name: "RETRO TTS",
    primary: "#FF0000",
    secondary: "#00FFFF",
    accent: "#00FF00",
    dim: "#666666",
    saying: "Bright lights, big city, amazing dictation",
  },
  midnight: {
    name: "RETRO TTS",
    primary: "#00CCFF",
    secondary: "#0066FF",
    accent: "#00DDFF",
    dim: "#003366",
    saying: "Professional speech-to-text in azure dreams",
  },
};

interface AnimatedTerminalProps {
  theme: keyof typeof themes;
  demoText?: string;
}

export const AnimatedTerminal: React.FC<AnimatedTerminalProps> = ({
  theme = "cyberpunk",
  demoText
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const themeConfig = themes[theme];
  const displayText = demoText || themeConfig.saying;

  // REC indicator blink (every 30 frames = 1 second at 30fps)
  const recBlink = Math.floor(frame / 15) % 2 === 0;

  // Audio level animation (simulated VU meter)
  const audioLevel = interpolate(
    frame % 60,
    [0, 15, 30, 45, 60],
    [0.1, 0.7, 0.5, 0.8, 0.1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Typing animation for output text
  const typingProgress = spring({
    frame: frame - 90, // Start typing after 3 seconds
    fps,
    config: { damping: 200 },
  });

  const typedLength = Math.floor(typingProgress * displayText.length);
  const typedText = displayText.slice(0, typedLength);

  // Show cursor blink
  const cursorBlink = Math.floor(frame / 15) % 2 === 0;
  const showCursor = frame >= 90 && typedLength < displayText.length;

  // Status changes
  const status =
    frame < 60 ? "REC" :
    frame < 330 ? "REC" :
    "COMPLETE";

  const infoText =
    frame < 60 ? "Stop talking for 3s to finish" :
    frame < 330 ? "Stop talking for 3s to finish" :
    "Transcription complete!";

  return (
    <AbsoluteFill style={{ backgroundColor: "#000000" }}>
      {/* Main Container */}
      <div
        style={{
          width: "100%",
          height: "100%",
          padding: "20px",
          fontFamily: "monospace",
          fontSize: "14px",
          color: themeConfig.primary,
        }}
      >
        {/* Header */}
        <div
          style={{
            border: `2px solid ${themeConfig.primary}`,
            padding: "20px",
            marginBottom: "10px",
            textAlign: "center",
            boxShadow: `0 0 20px ${themeConfig.primary}`,
          }}
        >
          <pre
            style={{
              fontSize: "24px",
              color: themeConfig.secondary,
              textShadow: `0 0 10px ${themeConfig.secondary}, 0 0 20px ${themeConfig.secondary}`,
              lineHeight: 1.2,
              margin: 0,
              fontWeight: "bold",
            }}
          >
{`╔═══════════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗████████╗██████╗  ██████╗     ████████╗████████╗███████╗ ║
║  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝╚══██╔══╝██╔════╝ ║
║  ██████╔╝█████╗     ██║   ██████╔╝██║   ██║       ██║      ██║   ███████╗ ║
║  ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║       ██║      ██║   ╚════██║ ║
║  ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝       ██║      ██║   ███████║ ║
║  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝      ╚═╝   ╚══════╝ ║
╚═══════════════════════════════════════════════════════════════════════╝`}
          </pre>
        </div>

        {/* Main Content Area */}
        <div style={{ display: "flex", height: "calc(100% - 200px)" }}>
          {/* Left Panel - System Status */}
          <div
            style={{
              width: "30%",
              border: `2px solid ${themeConfig.accent}`,
              padding: "15px",
              marginRight: "10px",
              boxShadow: `0 0 10px ${themeConfig.accent}`,
            }}
          >
            <div
              style={{
                borderBottom: `1px solid ${themeConfig.accent}`,
                paddingBottom: "10px",
                marginBottom: "15px",
                color: themeConfig.accent,
                textAlign: "center",
              }}
            >
              ⚡ SYSTEM STATUS ⚡
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>STATUS:</span>{" "}
              <span
                style={{
                  color: recBlink && status === "REC" ? themeConfig.secondary : themeConfig.dim,
                  fontWeight: "bold",
                }}
              >
                ● {status}
              </span>
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>HOTKEY:</span>{" "}
              <span style={{ color: themeConfig.primary }}>Ctrl+Shift+Space</span>
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>LANGUAGE:</span>{" "}
              <span style={{ color: themeConfig.accent }}>en-US</span>
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>SILENCE:</span>{" "}
              <span style={{ color: themeConfig.accent }}>3.0s</span>
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>MAX TIME:</span>{" "}
              <span style={{ color: themeConfig.accent }}>120s</span>
            </div>

            <div style={{ marginBottom: "8px" }}>
              <span style={{ color: themeConfig.dim }}>DUCKING:</span>{" "}
              <span style={{ color: themeConfig.secondary }}>30%</span>
            </div>

            <div
              style={{
                marginTop: "20px",
                paddingTop: "10px",
                borderTop: `1px solid ${themeConfig.dim}`,
              }}
            >
              <div style={{ color: themeConfig.dim, marginBottom: "5px" }}>INFO:</div>
              <div style={{ color: themeConfig.accent, fontSize: "12px" }}>
                {infoText}
              </div>
            </div>
          </div>

          {/* Right Panel - Audio Input & Output */}
          <div style={{ width: "70%", display: "flex", flexDirection: "column" }}>
            {/* Audio Input VU Meter */}
            <div
              style={{
                border: `2px solid ${themeConfig.secondary}`,
                padding: "15px",
                marginBottom: "10px",
                height: "30%",
                boxShadow: `0 0 10px ${themeConfig.secondary}`,
              }}
            >
              <div
                style={{
                  borderBottom: `1px solid ${themeConfig.secondary}`,
                  paddingBottom: "10px",
                  marginBottom: "15px",
                  color: themeConfig.secondary,
                  textAlign: "center",
                }}
              >
                ▬▬▬ AUDIO INPUT ▬▬▬
              </div>

              {/* VU Meter */}
              <div
                style={{
                  width: "100%",
                  height: "30px",
                  border: `2px solid ${themeConfig.primary}`,
                  padding: "3px",
                  marginBottom: "15px",
                }}
              >
                <div
                  style={{
                    width: `${audioLevel * 100}%`,
                    height: "100%",
                    background: `linear-gradient(90deg, ${themeConfig.accent}, ${themeConfig.primary})`,
                    transition: "width 0.1s",
                    boxShadow: `0 0 10px ${themeConfig.primary}`,
                  }}
                />
              </div>

              <div style={{ textAlign: "center" }}>
                <span style={{ color: themeConfig.dim }}>LEVEL: </span>
                <span
                  style={{
                    color: themeConfig.secondary,
                    fontWeight: "bold",
                    fontSize: "20px",
                  }}
                >
                  {Math.floor(audioLevel * 100)}%
                </span>
                <span
                  style={{
                    marginLeft: "20px",
                    color: audioLevel < 0.3 ? themeConfig.dim : themeConfig.accent,
                  }}
                >
                  {audioLevel < 0.3 ? "TOO QUIET" : audioLevel < 0.7 ? "OPTIMAL" : "LOUD"}
                </span>
              </div>
            </div>

            {/* Transcribed Output */}
            <div
              style={{
                border: `2px solid ${themeConfig.accent}`,
                padding: "15px",
                flex: 1,
                boxShadow: `0 0 10px ${themeConfig.accent}`,
              }}
            >
              <div
                style={{
                  borderBottom: `1px solid ${themeConfig.accent}`,
                  paddingBottom: "10px",
                  marginBottom: "15px",
                  color: themeConfig.accent,
                  textAlign: "center",
                }}
              >
                ✎ TRANSCRIBED OUTPUT ✎
              </div>

              <div
                style={{
                  color: themeConfig.primary,
                  fontSize: "16px",
                  lineHeight: 1.6,
                  minHeight: "100px",
                }}
              >
                {frame < 90 ? (
                  <span style={{ color: themeConfig.dim, fontStyle: "italic" }}>
                    [ Awaiting input... ]
                  </span>
                ) : (
                  <>
                    {typedText}
                    {showCursor && cursorBlink && (
                      <span style={{ color: themeConfig.secondary }}>█</span>
                    )}
                  </>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
