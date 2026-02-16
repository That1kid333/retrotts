import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, Sequence, staticFile } from "remotion";

interface CardData {
  title: string;
  description: string;
  imagePosition: string; // CSS background-position to show different parts of landscape
  glowColor: string;
  delay: number;
}

const cards: CardData[] = [
  {
    title: "6 EPIC THEMES",
    description: "Cyberpunk • Matrix • Vaporwave\nAmber • Neon • Midnight",
    imagePosition: "center 20%", // Sky/nebula portion
    glowColor: "#ff00ff",
    delay: 0,
  },
  {
    title: "SYSTEM-WIDE HOTKEY",
    description: "Ctrl+Shift+Space\nWorks in ANY application",
    imagePosition: "center 45%", // Mountain peaks
    glowColor: "#00ffff",
    delay: 20,
  },
  {
    title: "REAL-TIME VU METER",
    description: "Visual audio feedback\nAuto-volume ducking",
    imagePosition: "center 65%", // Mid-mountains
    glowColor: "#00ff00",
    delay: 40,
  },
  {
    title: "100% FREE FOREVER",
    description: "Open source • No ads\nNo hidden costs",
    imagePosition: "center 85%", // Forest/lake reflection
    glowColor: "#ffaa00",
    delay: 60,
  },
];

const HolographicCard: React.FC<{
  card: CardData;
  startFrame: number;
}> = ({ card, startFrame }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const relativeFrame = frame - startFrame;

  // Entrance animation
  const opacity = interpolate(relativeFrame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const translateY = interpolate(relativeFrame, [0, 30], [50, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const scale = interpolate(relativeFrame, [0, 25], [0.8, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Floating animation
  const floatY = interpolate(
    (relativeFrame % 120) / 120,
    [0, 0.5, 1],
    [0, -10, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Glow pulse animation
  const glowIntensity = interpolate(
    (relativeFrame % 90) / 90,
    [0, 0.5, 1],
    [0.6, 1, 0.6],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Corner accent animation
  const cornerGlow = interpolate(
    (relativeFrame % 60) / 60,
    [0, 0.5, 1],
    [0.3, 1, 0.3]
  );

  return (
    <div
      style={{
        width: 380,
        height: 280,
        position: "relative",
        opacity,
        transform: `translateY(${translateY + floatY}px) scale(${scale})`,
      }}
    >
      {/* Outer glow */}
      <div
        style={{
          position: "absolute",
          inset: -20,
          background: `radial-gradient(ellipse at center, ${card.glowColor}${Math.floor(glowIntensity * 40).toString(16).padStart(2, '0')}, transparent 70%)`,
          filter: "blur(20px)",
        }}
      />

      {/* Card container with steampunk border */}
      <div
        style={{
          position: "relative",
          width: "100%",
          height: "100%",
          background: "rgba(0, 0, 0, 0.7)",
          border: `3px solid ${card.glowColor}`,
          boxShadow: `
            0 0 20px ${card.glowColor}${Math.floor(glowIntensity * 100).toString(16).padStart(2, '0')},
            inset 0 0 20px rgba(0, 0, 0, 0.8)
          `,
          clipPath: "polygon(0 0, 100% 0, 100% calc(100% - 20px), calc(100% - 20px) 100%, 0 100%)",
        }}
      >
        {/* Landscape background (cropped portion) */}
        <div
          style={{
            position: "absolute",
            inset: 0,
            backgroundImage: `url(${staticFile('images/cyberpunk-landscape.jpg')})`,
            backgroundSize: "cover",
            backgroundPosition: card.imagePosition,
            opacity: 0.3,
            filter: "blur(1px)",
          }}
        />

        {/* Corner accents (steampunk rivets) */}
        <div
          style={{
            position: "absolute",
            top: 10,
            left: 10,
            width: 15,
            height: 15,
            borderRadius: "50%",
            background: `radial-gradient(circle, ${card.glowColor}, transparent)`,
            boxShadow: `0 0 ${10 * cornerGlow}px ${card.glowColor}`,
          }}
        />
        <div
          style={{
            position: "absolute",
            top: 10,
            right: 10,
            width: 15,
            height: 15,
            borderRadius: "50%",
            background: `radial-gradient(circle, ${card.glowColor}, transparent)`,
            boxShadow: `0 0 ${10 * cornerGlow}px ${card.glowColor}`,
          }}
        />
        <div
          style={{
            position: "absolute",
            bottom: 10,
            left: 10,
            width: 15,
            height: 15,
            borderRadius: "50%",
            background: `radial-gradient(circle, ${card.glowColor}, transparent)`,
            boxShadow: `0 0 ${10 * cornerGlow}px ${card.glowColor}`,
          }}
        />

        {/* Diagonal corner cut decoration */}
        <div
          style={{
            position: "absolute",
            bottom: 0,
            right: 0,
            width: 20,
            height: 20,
            borderTop: `2px solid ${card.glowColor}`,
            borderLeft: `2px solid ${card.glowColor}`,
            boxShadow: `0 0 10px ${card.glowColor}`,
          }}
        />

        {/* Content */}
        <div
          style={{
            position: "relative",
            width: "100%",
            height: "100%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            padding: 30,
            fontFamily: "monospace",
          }}
        >
          {/* Title */}
          <h2
            style={{
              fontSize: 32,
              fontWeight: "bold",
              color: card.glowColor,
              textShadow: `0 0 10px ${card.glowColor}, 0 0 20px ${card.glowColor}`,
              marginBottom: 20,
              textAlign: "center",
              letterSpacing: 2,
            }}
          >
            {card.title}
          </h2>

          {/* Description */}
          <p
            style={{
              fontSize: 18,
              color: "#ffffff",
              textShadow: `0 0 5px ${card.glowColor}`,
              textAlign: "center",
              lineHeight: 1.6,
              whiteSpace: "pre-line",
            }}
          >
            {card.description}
          </p>

          {/* Scanline effect */}
          <div
            style={{
              position: "absolute",
              inset: 0,
              background: `repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0, 0, 0, 0.1) 2px,
                rgba(0, 0, 0, 0.1) 4px
              )`,
              pointerEvents: "none",
            }}
          />
        </div>
      </div>
    </div>
  );
};

export const HolographicCards: React.FC = () => {
  const { width, height, durationInFrames } = useVideoConfig();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#000000",
        display: "grid",
        gridTemplateColumns: "repeat(2, 1fr)",
        gridTemplateRows: "repeat(2, 1fr)",
        gap: 40,
        padding: 60,
        alignItems: "center",
        justifyItems: "center",
      }}
    >
      {cards.map((card, index) => (
        <Sequence key={card.title} from={card.delay}>
          <HolographicCard
            card={card}
            startFrame={card.delay}
          />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
