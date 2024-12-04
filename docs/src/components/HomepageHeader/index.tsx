import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { buttonVariants } from "@site/src/components/ui/button";
import { motion, useViewportScroll, useTransform } from "framer-motion";
import { FaAngleRight } from "react-icons/fa6";
import styles from "./index.module.scss";

// Utility function for animated subtitle letters with correct word spacing
const generateSubtitle = (tagline: string) =>
	tagline.split("").map((char, index) => {
		if (char === " ") {
			return <span key={index} className="inline-block w-2" />;
		}

		return (
			<motion.span
				key={index}
				className={`${styles.subtitleLetter} inline-block`}
				initial={{ y: 50, opacity: 0, rotate: 15, scale: 0.8 }}
				animate={{ y: 0, opacity: 1, rotate: 0, scale: 1 }}
				whileHover={{ scale: 1.15, color: "#ff69b4" }} // Increased hover scale for better interaction
				transition={{
					delay: index * 0.05,
					type: "spring",
					stiffness: 120,
					damping: 10,
				}}
			>
				{char}
			</motion.span>
		);
	});

export default function HomepageHeader(): JSX.Element {
	// Add scroll-dependent animations
	const { scrollY } = useViewportScroll();
	const yPosition = useTransform(scrollY, [0, 300], [0, -50]);

	// Parallax effect for the background
	const parallaxY = useTransform(scrollY, [0, 500], [0, -100]);

	const { siteConfig } = useDocusaurusContext();
	const subtitle = generateSubtitle(siteConfig.tagline);

	return (
		<motion.header
			className={`${styles.heroBanner} relative overflow-hidden text-center`}
			style={{ y: parallaxY }}
			initial={{ opacity: 0.7, y: -50 }}
			animate={{ opacity: 1, y: 0 }}
			whileHover={{ scale: 1.02 }}
			transition={{ duration: 0.5 }}
		>
			<div
				className={`${styles.hero__container} container mx-auto flex flex-col items-center justify-center w-full px-4 md:px-8 lg:px-16 z-10`}
			>
				<motion.img
					src="img/icon.webp"
					alt="Site icon"
					className={`${styles.hero__logo} h-24 w-auto mb-6 md:h-32 md:mb-8 lg:h-40 lg:mb-10`}
					initial={{ scale: 0, rotate: -180 }}
					animate={{ scale: 1, rotate: 0 }}
					whileHover={{ rotate: [0, 360] }}
					transition={{ duration: 2, ease: "easeInOut" }}
				/>
				<motion.h1
					className={`${styles.hero__title} text-4xl md:text-5xl lg:text-6xl font-extrabold`}
					initial={{ opacity: 0, y: -20 }}
					animate={{ opacity: 1, y: 0 }}
					transition={{ duration: 1.2, ease: "easeOut" }}
				>
					{siteConfig.title}
				</motion.h1>
				<p className={`${styles.hero__subtitle}`}>{subtitle}</p>
				<div
					className={`${styles.buttons} flex items-center justify-center mb-4`}
				>
					<motion.div
						whileHover={{
							scale: 1.1,
							boxShadow: "0px 0px 20px rgba(255, 255, 255, 0.6)",
						}}
						whileTap={{ scale: 0.95 }}
					>
						<Link
							to="/docs"
							aria-label="Get Started"
							className={`${styles.landingButton} ${buttonVariants({ variant: "outline" })}`}
						>
							Get Started
							<FaAngleRight className={styles.button__icon} />
						</Link>
					</motion.div>
				</div>
				<motion.hr
					className={`${styles.heroDivider} mt-8 w-1/2`}
					initial={{ width: "0%" }}
					animate={{ width: "150%" }}
					transition={{ duration: 1.0, ease: "easeInOut" }}
				/>
			</div>
		</motion.header>
	);
}
