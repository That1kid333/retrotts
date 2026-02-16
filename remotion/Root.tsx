import { Composition } from "remotion";
import { ThemeShowcase } from "./Videos/ThemeShowcase";
import { ThemeComparison } from "./Videos/ThemeComparison";
import { HowToUse } from "./Videos/HowToUse";
import { MatrixTheme } from "./Videos/MatrixTheme";
import { VaporwaveTheme } from "./Videos/VaporwaveTheme";
import { AmberTheme } from "./Videos/AmberTheme";
import { NeonTheme } from "./Videos/NeonTheme";
import { MidnightTheme } from "./Videos/MidnightTheme";
import { CyberpunkTheme } from "./Videos/CyberpunkTheme";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Main Showcase - All Themes Loop */}
      <Composition
        id="ThemeShowcase"
        component={ThemeShowcase}
        durationInFrames={900} // 30 seconds at 30fps
        fps={30}
        width={1920}
        height={1080}
      />

      {/* Theme Comparison */}
      <Composition
        id="ThemeComparison"
        component={ThemeComparison}
        durationInFrames={1350} // 45 seconds
        fps={30}
        width={1920}
        height={1080}
      />

      {/* Tutorial Video */}
      <Composition
        id="HowToUse"
        component={HowToUse}
        durationInFrames={1800} // 60 seconds
        fps={30}
        width={1920}
        height={1080}
      />

      {/* Individual Theme Videos (15 seconds each) */}
      <Composition
        id="CyberpunkDemo"
        component={CyberpunkTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="MatrixDemo"
        component={MatrixTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="VaporwaveDemo"
        component={VaporwaveTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="AmberDemo"
        component={AmberTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="NeonDemo"
        component={NeonTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />

      <Composition
        id="MidnightDemo"
        component={MidnightTheme}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
