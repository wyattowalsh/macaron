// macaron/docs/src/components/DocsFeatures.tsx -- component for the features section on the docs homepage

import Link from "@docusaurus/Link";
import {
	Tooltip,
	TooltipContent,
	TooltipProvider,
	TooltipTrigger,
} from "@site/src/components/ui/tooltip";
import { TooltipArrow } from "@radix-ui/react-tooltip";
import { motion } from "framer-motion";
import React from "react";

const features = [
	{
		image: "/img/icons/pyenv.svg",
		alt: "pyenv",
		text: "Python version management with pyenv",
		docLink: "/docs/tools/pyenv",
		linkText: "Learn more about pyenv",
	},
	{
		image: "/img/icons/poetry.svg",
		alt: "Poetry",
		text: "Dependency management with Poetry",
		docLink: "/docs/tools/poetry",
		linkText: "Learn more about Poetry",
	},
	{
		image: "/img/icons/pytest.svg",
		alt: "Pytest",
		text: "Testing with Pytest",
		docLink: "/docs/tools/pytest",
		linkText: "Learn more about Pytest",
	},
	{
		image: "/img/icons/docusaurus.svg",
		alt: "Docusaurus",
		text: "Docs site with Docusaurus",
		docLink: "/docs/tools/docusaurus",
		linkText: "Learn more about Docusaurus",
	},
	{
		image: "/img/icons/yapf.svg",
		alt: "YAPF",
		text: "Formatting with customized YAPF",
		docLink: "/docs/tools/yapf",
		linkText: "Learn more about YAPF",
	},
	{
		image: "/img/icons/ruff.svg",
		alt: "Ruff",
		text: "Linting with Ruff",
		docLink: "/docs/tools/ruff",
		linkText: "Learn more about Ruff",
	},
	{
		image: "/img/icons/makefile.svg",
		alt: "Makefile",
		text: "Automation via Makefile",
		docLink: "/docs/tools/makefile",
		linkText: "Learn more about Makefile",
	},
	{
		image: "/img/icons/github-actions.svg",
		alt: "GitHub Actions",
		text: "CI/CD with GitHub Actions",
		docLink: "/docs/tools/github-actions",
		linkText: "Learn more about GitHub Actions",
	},
	{
		image: "/img/icons/tools.svg",
		alt: "Tools",
		text: 'See all of the tools <img src="/img/icons/enter.svg" alt="Enter" class="h-8 w-8 inline-block" />',
		docLink: "/docs/tools",
		linkText: "Discover all tools",
	},
];

const FeatureCard = ({ image, alt, text, docLink, linkText }) => (
	<motion.div
		whileHover={{
			scale: 1.05,
			rotate: 0.5,
			boxShadow: "0px 10px 20px rgba(0, 0, 0, 0.2)",
		}}
		className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition-transform"
	>
		<TooltipProvider>
			<Tooltip>
				<TooltipTrigger>
					<Link to={docLink} className="flex items-center space-x-4">
						<motion.img
							src={image}
							alt={alt}
							className="h-16 w-16 transition-transform duration-300 ease-in-out transform"
							whileHover={{ rotate: [0, -10, 10, -10, 10, 0], scale: 1.2 }}
						/>
						<div>
								<div
								className="text-lg font-medium text-gray-900 dark:text-gray-100"
								dangerouslySetInnerHTML={{ __html: text }}
							/>
						</div>
					</Link>
				</TooltipTrigger>
				<TooltipContent
					side="bottom"
					align="center"
					sideOffset={5}
					className="bg-gray-800 text-white p-2 rounded-md shadow-lg"
				>
					<p>{linkText}</p>
					<TooltipArrow className="fill-gray-800" />
				</TooltipContent>
			</Tooltip>
		</TooltipProvider>
	</motion.div>
);

const DocsFeatures = () => {
	const containerVariants = {
		hidden: {},
		show: {
			transition: {
				staggerChildren: 0.1,
			},
		},
	};

	const itemVariants = {
		hidden: { opacity: 0, y: 20 },
		show: { opacity: 1, y: 0 },
	};

	return (
		<motion.div
			className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
			variants={containerVariants}
			initial="hidden"
			animate="show"
		>
			{features.map((feature, index) => (
				<motion.div variants={itemVariants} key={index}>
					<FeatureCard {...feature} />
				</motion.div>
			))}
		</motion.div>
	);
};

export default DocsFeatures;
