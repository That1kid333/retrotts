import { Composition } from "remotion";
import { AnimatedTerminal } from "./Videos/AnimatedTerminal";
import { CyberpunkTheme } from "./Videos/CyberpunkTheme";
import { MatrixTheme } from "./Videos/MatrixTheme";
import { VaporwaveTheme } from "./Videos/VaporwaveTheme";
import { AmberTheme } from "./Videos/AmberTheme";
import { NeonTheme } from "./Videos/NeonTheme";
import { MidnightTheme } from "./Videos/MidnightTheme";
import { AllThemesShowcase } from "./Videos/AllThemesShowcase";
import { HolographicCards } from "./Videos/HolographicCards";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* 🌟 MAIN SHOWCASE - All 6 Themes in One Video! */}
      <Composition
        id="AllThemesShowcase"
        component={AllThemesShowcase}
        durationInFrames={2700} // 90 seconds (15s × 6 themes)
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{}}
      />

      {/* Individual Theme Videos (15 seconds each) */}
      <Composition
        id="Cyberpunk"
        component={CyberpunkTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="Matrix"
        component={MatrixTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="Vaporwave"
        component={VaporwaveTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="Amber"
        component={AmberTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="Neon"
        component={NeonTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="Midnight"
        component={MidnightTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      {/* Quick 30-second Teaser (first 5 seconds of each theme) */}
      <Composition
        id="QuickTeaser"
        component={AllThemesShowcase}
        durationInFrames={900} // 30 seconds
        fps={30}
        width={1920}
        height={1080}
      />

      {/* 🌟 HOLOGRAPHIC CARDS - Steampunk animated info cards */}
      <Composition
        id="HolographicCards"
        component={HolographicCards}
        durationInFrames={300} // 10 seconds
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{}}
      />
    </>
  );
};
